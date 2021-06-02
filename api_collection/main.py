#@author Phillip Simmonds
from api_connectors import mpi_opendata

def main():
    mpi_opendata.collect_mpi_data()

if __name__ == "__main__":
    main()

