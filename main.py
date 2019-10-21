import sys
import server


def main():
    host = ""
    try:
        port = sys.argv[1]
    except IndexError:
        port = 8080
    srv = server.Web(port)
    srv.start()



if __name__ == '__main__':
    main()
