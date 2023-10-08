from common.extension import Extension


class Gatherer(Extension):
    def setup(self, parser, actions, config, root):
        parser.add_argument("--console", help="Example argument for console gatherer")
        actions["console"] = self.run

    def run(self, args):
        print(f"console gatherer executed with argument: {args.console}")
