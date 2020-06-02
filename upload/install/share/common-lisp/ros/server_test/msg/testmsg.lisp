; Auto-generated. Do not edit!


(cl:in-package server_test-msg)


;//! \htmlinclude testmsg.msg.html

(cl:defclass <testmsg> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (age
    :reader age
    :initarg :age
    :type cl:integer
    :initform 0))
)

(cl:defclass testmsg (<testmsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <testmsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'testmsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name server_test-msg:<testmsg> is deprecated: use server_test-msg:testmsg instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <testmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader server_test-msg:name-val is deprecated.  Use server_test-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'age-val :lambda-list '(m))
(cl:defmethod age-val ((m <testmsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader server_test-msg:age-val is deprecated.  Use server_test-msg:age instead.")
  (age m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <testmsg>) ostream)
  "Serializes a message object of type '<testmsg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let* ((signed (cl:slot-value msg 'age)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <testmsg>) istream)
  "Deserializes a message object of type '<testmsg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'age) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<testmsg>)))
  "Returns string type for a message object of type '<testmsg>"
  "server_test/testmsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'testmsg)))
  "Returns string type for a message object of type 'testmsg"
  "server_test/testmsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<testmsg>)))
  "Returns md5sum for a message object of type '<testmsg>"
  "83da5ca00b8e049b0559653a472c88a5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'testmsg)))
  "Returns md5sum for a message object of type 'testmsg"
  "83da5ca00b8e049b0559653a472c88a5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<testmsg>)))
  "Returns full string definition for message of type '<testmsg>"
  (cl:format cl:nil "string name~%int32 age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'testmsg)))
  "Returns full string definition for message of type 'testmsg"
  (cl:format cl:nil "string name~%int32 age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <testmsg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <testmsg>))
  "Converts a ROS message object to a list"
  (cl:list 'testmsg
    (cl:cons ':name (name msg))
    (cl:cons ':age (age msg))
))
