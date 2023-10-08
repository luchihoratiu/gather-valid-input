from common.extension import Extension


class Validator(Extension):
    def setup(self, parser, actions, config, root):
        parser.add_argument(
            "--validator", help="Example argument for GitLab credentials validator"
        )
        actions["validator"] = self.run

    def run(self, args):
        print(f"GitLab credentials validator executed with argument: {args.validator}")
