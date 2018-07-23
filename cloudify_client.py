from cloudify_rest_client import CloudifyClient

client = CloudifyClient(host='host_ip', username='user', password='password', tenant='tenant')
blueprints = client.blueprints.list()
deplo_client = client.deployments
execution = client.executions
node_info=client.node_instances
for blueprint in blueprints:
   if (blueprint.id == 'monet'):
      bp = blueprint.id
deplo_id = 'example'
#create a deployment
deplo1 = deplo_client.create(bp,deplo_id)
#print deplo1
#deplor1= execution.start(deplo_id, 'create_deployment_environment')
#deplor1= execution.start(deplo_id, 'create_deployment_install')
#print node_info.list()
#nodes=node_info.list()
#for node in nodes:
#   print "NODE: ", node
for deplo in deplo_client.list():
   print "Deployment: ", deplo


#deplo_client.delete(deplo_id)

