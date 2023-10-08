from common.extension import Extension


class Gatherer(Extension):
    def setup(self, parser, actions, config, root):
        parser.add_argument("--gatherer", help="Example argument for dotenv gatherer")
        actions["gatherer"] = self.run

    def run(self, args):
        print(f"dotenv gatherer executed with argument: {args.example}")
