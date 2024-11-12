class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        # lisätään ranskalaiset viivat taulukon alkioihin
        authors = list(map(lambda x: "- " + x, self.authors))
        deps = list(map(lambda x: "- " + x, self.dependencies))
        devDeps = list(map(lambda x: "- " + x, self.dev_dependencies))

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n\n"

            "Authors:\n"
            f"{"\n".join(authors)}\n\n"

            "Dependencies:\n"
            f"{"\n".join(deps)}\n\n"

            "Development dependencies:\n"
            f"{"\n".join(devDeps)}\n"
        )
