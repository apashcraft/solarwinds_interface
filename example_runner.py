import getpass
from solarwinds_interface.sw_interface import SolarWindsInterface
from tools.tools import Tools


def main():
    csv_path = "data/example_nodes.csv"
    tool_bag = Tools()

    # Set keys = None if you're not using IN in your query
    # Otherwise, provide csv file with node names at given index
    keys = tool_bag.csv_pull_key(csv_path, 0)

    # Put your query here
    query_str = """SELECT TOP 10 NodeName, NodeID, Uri
                   FROM Orion.Nodes
                   WHERE NodeName IN %s"""
    # Put your suppression dates here
    suppress_start = '04/28/2019 08:00 AM'
    suppress_end = '04/28/2019 08:01 AM'

    #updated_props = {'City': None}

    # Authentication
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    server = "solarwinds.server"
    sw = SolarWindsInterface(username, password, server)

    # Send your query.
    sw.query(query_str, nodes=keys)
    # Suppress alerts
    sw.suppress_alerts(suppress_start, suppress_end)

    print("Exit status complete")


if __name__ == '__main__':
    main()
