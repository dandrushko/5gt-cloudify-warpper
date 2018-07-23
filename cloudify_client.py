from cloudify_rest_client import CloudifyClient
from cloudify_rest_client.exceptions import IllegalExecutionParametersError


'''

Per Jordi request the following functionality has to be available at Cloudify wrapper:
-List the available blueprints
-List current deployments
-Create a network service (in this case we consider create a network service as: create the deployment and install it)
-Check the operational state of a deployment
-Delete a network service: in this case we consider delete a network service as: uninstall the deployment and remove
   the deployment from the list of deployments. 

'''

CLOUDIFY_HOST = '172.17.0.2'
CLOUDIFY_USER = 'admin'
CLOUDIFY_PASSWORD = 'admin'
TENANT = 'default_tenant'


client = CloudifyClient(host=CLOUDIFY_HOST, username=CLOUDIFY_USER, password=CLOUDIFY_PASSWORD, tenant=TENANT)


def list_blueprints():
    # Blueprints list has too much information, potentially only subset of this data is really required
    # so some filtering should be applied here
    return client.blueprints.list()


def list_blueprint_deployments(blueprint_id=None):
    """
    There might be multiple service deployments of the single blueprint
    :param blueprint_id - id of the blueprint used for deployment
    """
    if not blueprint_id:
        return


def install_service(blueprint_id=None, deployment_id=None):
    """
        Assuming blueprint was uploaded, this method triggers deployment creation and then 'install' workflow
        for specified deployment
        :param:
        :return:
    """
    if not blueprint_id or not deployment_id:
        return
    # Creating deployment
    create_deployment_response = client.deployments.create(blueprint_id=blueprint_id, deployment_id=deployment_id)

    # Launching 'install' workflow on a specified deployment
    try:
        response = client.executions.start(deployment_id=deployment_id, workflow_id='install')
    except IllegalExecutionParametersError:
        return IllegalExecutionParametersError.ERROR_CODE
    return {'deployment_id': response.deployment_id, 'execution_id': response.id, 'status': response.status }


def check_deployment_status(deployment_id=None):
    if not deployment_id:
        return
    return client.executions.list(deployment_id=deployment_id)


def uninstall_deployment(deployment_id=None):
    """
    Removes specified deployment. At this moment it just sends delete command and returns async result. However
    to get actual status, appropriate execution id should be tracked
    :param deployment_id:
    :return: Deployment object
    """
    if not deployment_id:
        return
    return client.deployments.delete(deployment_id=deployment_id,ignore_live_nodes=True)


if __name__ == '__main__':

    for item in check_deployment_status('new1'):
        print item
    raw_input()

    print install_service('vnf-docker', 'new1')
    raw_input()
    print check_deployment_status('new1')
    print uninstall_deployment('new1')
    raw_input()
    print check_deployment_status('new1')
