# coding:utf-8
"""
Creates deployment, service for the image.
"""
import time

from kubernetes import client, config


def create_deployment(apps_v1_api, image, deployment_name,label):
    container = client.V1Container(
        name="cloudroid-instance",
        image=image,
        image_pull_policy="Never",
        ports=[client.V1ContainerPort(container_port=9090)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels=label),
        spec=client.V1PodSpec(containers=[container]))
    # Spec
    spec = client.V1DeploymentSpec(
        replicas=1,
        template=template,
        selector= client.V1LabelSelector(
            match_labels=label,
        )
    )
    # Deployment
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=deployment_name),
        spec=spec)
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    apps_v1_api.create_namespaced_deployment(
        namespace="cloudroid-swarm", body=deployment
    )


def create_service(deployment_name, label):
    core_v1_api = client.CoreV1Api()
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name=deployment_name
        ),
        spec=client.V1ServiceSpec(
            selector=label,
            ports=[client.V1ServicePort(
                port=9090,
                target_port=9090
            )]
        )
    )
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    core_v1_api.create_namespaced_service(namespace="cloudroid-swarm", body=body)

#  about k8s service
def get_clusterip(deployment_name):
    core_v1_api = client.CoreV1Api()
    service_list = core_v1_api.list_namespaced_service(namespace="cloudroid-swarm")
    for svc in service_list.items:
        print "existing deployment %s" % deployment_name
        if svc.metadata.name == deployment_name:
            return svc.spec.cluster_ip
    print "Can not find service using " + deployment_name
    return service_list
    #return service_list.items[0].spec.cluster_ip


# about k8s pod
def get_nodeip(deployment_name, label_selector):  # 有时候运行会返回None，导致程序错误。有待改善
    api_instance = client.CoreV1Api()
    # print pod_list
    # time.sleep(1)
    # while True:
    #     if deployment_name not in get_exist_deployment():
    #         print "Waiting for establishing deployment......"
    #         time.sleep(1)
    #     break
    while True:
        pod_list = api_instance.list_namespaced_pod(namespace="cloudroid-swarm", label_selector=label_selector)
        for pod in pod_list.items:
            if pod.status.host_ip:
                return pod.status.host_ip

def get_exist_deployment():
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    deployment_list = apps_v1_api.list_namespaced_deployment(namespace="cloudroid-swarm")
    exist_deployment = []
    for item in deployment_list.items:
        exist_deployment.append(item.metadata.name)
    return exist_deployment
    # return a list


def delete_deployment(deployment_name):
    # Delete deployment
    api_instance = client.AppsV1Api()
    api_response = api_instance.delete_namespaced_deployment(
        name=deployment_name,
        namespace="cloudroid-swarm",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground'))
    print("Deployment %s has been deleted. status='%s'" % (deployment_name, str(api_response.status)))


def delete_service(deployment_name):
    core_v1_api = client.CoreV1Api()
    api_response = core_v1_api.delete_namespaced_service(
        namespace="cloudroid-swarm",
        name=deployment_name
    )
    print("Service deleted. status='%s'" % str(api_response.status))

def main():
    # Fetching and loading local Kubernetes Information
    image = "ros:test"
    deployment_name = "cloudroid"
    config.load_kube_config()
    apps_v1_api = client.AppsV1Api()
    label = {"app": "cloudroid"}
    create_deployment(apps_v1_api, image=image, deployment_name=deployment_name,label=label)
    # create_service(deployment_name=deployment_name)
    #label_selector = "app=cloudroid"
    #print get_nodeip(label_selector=label_selector)


if __name__ == "__main__":
    main()

