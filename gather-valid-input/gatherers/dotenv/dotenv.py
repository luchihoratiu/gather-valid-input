class Gatherer:
    def setup(self, parser, action_dict):
        parser.add_argument("--gatherer", help="Example argument for dotenv gatherer")
        action_dict["gatherer"] = self.run

    def run(self, args):
        print(f"dotenv gatherer executed with argument: {args.example}")
