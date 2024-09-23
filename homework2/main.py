import sys

import requests


def generate_plantuml(graph):
    uml = "@startuml\n"
    for package, deps in graph.items():
        for dep in deps.keys():
            uml += f'"{package}" --> "{dep}"\n'
    uml += "@enduml\n"
    return uml


def get_npm_dependencies(package_name):
    url = f'https://registry.npmjs.org/{package_name}'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch package data: {response.status_code}")

    package_data = response.json()
    latest_version = package_data['dist-tags']['latest']
    dependencies = package_data['versions'][latest_version].get('dependencies', {})
    return dependencies


def get_transitive_dependencies(package_name, collected):
    if package_name in collected:
        return collected
    dependencies = get_npm_dependencies(package_name)
    collected[package_name] = dependencies
    for dep in dependencies:
        get_transitive_dependencies(dep, collected)
    return collected


# Получение всех зависимостей, включая транзитивные:
all_dependencies = get_transitive_dependencies(sys.argv[1], {})
print(generate_plantuml(all_dependencies))
