import logging
import webview

from server import server

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    window = webview.create_window('学生管理系统', server)
    webview.start(debug=True)
