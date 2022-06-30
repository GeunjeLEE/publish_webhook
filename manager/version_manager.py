import yaml

class VersionManager():
    def __init__(self):
        pass

    def run(self, image_name, tag):
        version_file = {
            image_name: {
                'image' : {
                    'name' : f'public.ecr.aws/megazone/spaceone/{image_name}',
                    'version' : tag
                }
            }
        }

        try:
            with open(f'./tmp/{image_name}.yaml', 'w') as f:
                yaml.dump(version_file, f)
            return 200
        except Exception as e:
            return 500