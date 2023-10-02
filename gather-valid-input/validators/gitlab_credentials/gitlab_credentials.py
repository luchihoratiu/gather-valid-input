class Validator:
    def setup(self, parser, action_dict):
        parser.add_argument(
            "--validator", help="Example argument for GitLab credentials validator"
        )
        action_dict["validator"] = self.run

    def run(self, args):
        print(f"GitLab credentials validator executed with argument: {args.validator}")
