from darkroom.interfaces.developments.darkroom_development import IDarkRoomDevelopment
from darkroom.exposure_parser import ParsedData

class ImageDevelopment():
    def __init__(self, data : DarkRoomProject, development: IDarkRoomDevelopment,
                 os_ops: IDarkRoomOsOperations):
        self.data = data
        self.development = development
        self.os_ops = os_ops

    def setup(self):
        try:
            for build_dir in self.data.build_dirs:
                self.validate_images(build_dir.images)
                self.init_transports(build_dir.images)
        except Exception as e:
             print(f"Failed to setup image development: {e}")

    def teardown(self):
        self.development.teardown()

    def put_images(self):
        self.development.push_images()

    def pull_images(self, project):
        pull_path = project.pull_path
        if not pull_path:
            pull_path = project.project_path
        self.development.pull_images(pull_path)

    def validate_images(self, images):
        for image in images:
            self.check_image_exists("source", image.source_path)

    def check_image_exists(self,name, path):
        if not self.os_ops.file_exists(path):
            raise Exception(f"Invalid images: {name} at path {path} does not exist ")

    def init_transports(self, images):
        for transport in self.data.transports:
            if transport.transport_type == self.development.transport_id:
                print(f"Init transports is {transport}")
                self.development.setup(images, transport.data)
