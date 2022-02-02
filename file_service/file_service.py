class FileService:
    @staticmethod
    def clean_file(file):
        open(file, 'w').close()

    @classmethod
    def write_list_to_file(cls, file, items):
        cls.clean_file(file)
        file = open(file, "a")
        for item in items:
            file.write(item)
            file.write("\n")
        file.close()

    @classmethod
    def number_of_line_in_file(cls, file):
        return len(cls.read_lines(file))

    @staticmethod
    def read_lines(file):
        file = open(file)
        return file.read().splitlines()
