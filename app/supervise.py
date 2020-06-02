# coding:utf-8
# !/usr/bin/python
# Software License Agreement (BSD License)
#
# Copyright (c) 2016, micROS Team
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of micROS-drt nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import threading
from dockerops import removeDeployment
import time
from app import db, models
from deploy_svc_create import get_exist_deployment
#from models import Services





mutex = threading.Lock()


class abandoned_service(threading.Thread):  # Find the abandoned service to remove
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        mutex.acquire()
        while True:
            deployments = get_exist_deployment()
            all_deployments = []
            all_deployments_class = models.Deployment.query.all()
            for i in all_deployments_class:
                all_deployments.append(i.deployment_name)
            # print deployments
            # print all_deployments
            for d in all_deployments:
                if d not in deployments:
                    removeDeployment(d)
            time.sleep(10)
            # print 'checking from supervise.py 0000000000000000'

            # for c in Deployments:
            #     if time.time() - float(c.createdtime) > 600:
            #         removeDeployment(c.deployment_name)
            #         print "Stopped %s" % c.deployment_name
            # time.sleep(10)

        mutex.release()