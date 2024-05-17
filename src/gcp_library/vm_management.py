from robot.api.deco import keyword
from google.cloud import compute_v1

class VMManagement:
    """
    This module is used for managing virtual machines in Google Cloud Platform.
    """
    def __init__(self):
        self.compute_client = compute_v1.InstancesClient()

    @keyword("Create VM Instance")
    def create_vm_instance(self, project_id, zone, instance_name):
        """
        Create a new Google Compute Engine instance.
        """
        instance = compute_v1.Instance()
        instance.name = instance_name
        instance.machine_type = f"zones/{zone}/machineTypes/e2-medium"

        # Specify the disk and image to use.
        disk = compute_v1.AttachedDisk()
        disk.initialize_params.project = project_id
        disk.initialize_params.source_image = "projects/debian-cloud/global/images/family/debian-10"
        disk.auto_delete = True
        disk.boot = True
        instance.disks = [disk]

        # Specify the network interface.
        network_interface = compute_v1.NetworkInterface()
        network_interface.name = "global/networks/default"
        instance.network_interfaces = [network_interface]

        # Create the instance.
        operation = self.compute_client.insert(
            project=project_id,
            zone=zone,
            instance_resource=instance)
        return operation.result()

    @keyword("List VM Instances")
    def list_vm_instances(self, project_id, zone):
        """
        List all instances in a given project and zone.
        """
        instances = self.compute_client.list(project=project_id, zone=zone)
        return [instance.name for instance in instances]
