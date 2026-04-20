import click
from exposure_parser import ExposureParser
from os_operations import OsOperations
from darkroom_os.os_pathlib import PathlibOsOperations

# TODO: integrate with click to pass context
# @click.command()
# @click.option('--server', help="Server to upload image too")
# @click.option('--target', help="Target for testing the images")
# @click.option('--images', help="Files to upload in the build directory")
# @click.option('--dest-images', help="Name file should be called on the server")
def upload(os_ops, exposure_parser):
    print("Test parser_exposure")
    cwd = str(os_ops.get_current_directory())
    print("Cwd is " + cwd)
    exposure_parser.parse_exposure("test_mode", cwd)

if __name__ == "__main__":
    # Create OS operation objects
    pathlib_ops = PathlibOsOperations()
    os_ops = OsOperations(pathlib_ops)

    # Create Exposure Parser
    exposure_parser = ExposureParser(os_ops)

    # for now call upload
    upload(os_ops, exposure_parser)
