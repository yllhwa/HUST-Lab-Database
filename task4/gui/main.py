import logging
import webview

from server import server

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    window = webview.create_window('My first pywebview application', server)
    webview.start()