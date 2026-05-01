import click
from darkroom.exposure_parser import ExposureParser
from darkroom.os_operations import OsOperations
from darkroom.darkroom_os.os_pathlib import PathlibOsOperations
from darkroom.darkroom_parsers.yaml_parser import YamlExposureParser
from darkroom.development import ImageDevelopment
from darkroom.darkroom_developments.ssh_development import SSHDevelopment
from darkroom.darkroom_transports.ssh. ssh_fabric import SSHFabric
from darkroom.interfaces.transports.darkroom_transports import DarkRoomTransports

# TODO: integrate with click to pass context
# @click.command()
# @click.option('--server', help="Server to upload image too")
# @click.option('--target', help="Target for testing the images")
# @click.option('--images', help="Files to upload in the build directory")
# @click.option('--dest-images', help="Name file should be called on the server")


def develop():
    # Create OS operation objects
    pathlib_ops = PathlibOsOperations()
    os_ops = OsOperations(pathlib_ops)
    parser = YamlExposureParser()

    # Create Exposure Parser
    exposure_parser = ExposureParser(parser, os_ops)
    cwd = str(os_ops.get_current_directory())
    parsed_data = exposure_parser.parse_exposure(cwd, DarkRoomTransports.SSH)

    fabric = SSHFabric()
    ssh_dev = SSHDevelopment(fabric, os_ops)

    print(f"Parsed data is {parsed_data}")
    development = ImageDevelopment(parsed_data, ssh_dev, os_ops)
    # for now call upload
    print("Setup development")
    try:
        development.setup()
        development.put_images()
        development.pull_images(parsed_data)
        development.teardown()
    except Exception as e:
        print(f"Darkroom Development Failed with {e}")

if __name__ == "__main__":
    develop()
