from goby_sdk.V1.lib.base_page import BasePage


class HomePage(BasePage):

    def get_poc_list(self, query="vultype=2", reload_pocs=False,
                     order_by={"vul_nums": "desc", "level": "desc", "host_nums": "desc"}, page=1, size=3000):
        data = {
            "query": query,
            "options": {
                "reloadPocs": reload_pocs,
                "order": order_by,
                "page": {
                    "page": page,
                    "size": size
                }
            }
        }
        return self._send_request("api/v1/getPOCList", data)

    def start_scan(self, task_name, ips, ports="0-65535", black_ips=[], vul_type="0", pocs_hosts={}, options={}):
        """
        开始扫描任务
        :param task_name: 扫描任务名称
        :type task_name: str
        :param ips: 目标IP列表，多个IP以逗号分隔
        :type ips: str
        :param ports: 扫描端口范围，默认为"0-65535"
        :type ports: str
        :param black_ips: 黑名单IP列表，多个IP以逗号分隔，默认为空列表
        :type black_ips: list
        :param vul_type: 漏洞类型，默认为"0"，可选值为"0"（全部）、"1"（高危）、"2"（中危）、"3"（低危）
        :type vul_type: str
        :param pocs_hosts: POC插件列表，为空字典则使用系统内置插件，可通过get_poc_list方法获取插件列表
        :type pocs_hosts: dict
        :param options: 扫描选项，为字典类型，可配置的选项请参考API文档
        :type options: dict
        :return: 返回扫描任务信息的JSON对象
        :rtype: dict
        """
        asset = {"ips": ips.split(","), "ports": ports, "blackIps": black_ips}
        vulnerability = {"type": vul_type, "pocs_hosts": pocs_hosts}
        data = {"taskName": task_name, "asset": asset, "vulnerability": vulnerability, "options": options}
        return self._send_request("api/v1/startScan", data)

    def get_scan_progress(self, task_id):
        """
        获取扫描任务进度信息

        :param task_id: 扫描任务ID
        :type task_id: str
        :return: 返回扫描任务进度信息的JSON对象
        :rtype: dict
        """
        data = {
            "taskId": task_id
        }
        return self._send_request("api/v1/getProgress", data)

    def resume_scan(self, task_id, options={}):
        """
        恢复扫描任务

        :param task_id: 任务ID
        :type task_id: str
        :param options: 扫描选项，默认为{"queue": 0, "random": True, "rate": 100, "portscanmode": 0, "screenshot": False, "extracthost": False, "deepAnalysis": True}
        :type options: dict
        :return: 返回操作结果的JSON对象
        :rtype: dict
        """
        default_options = {
            "queue": 0,
            "random": True,
            "rate": 100,
            "portscanmode": 0,
            "screenshot": False,
            "extracthost": False,
            "deepAnalysis": True
        }
        #合并字典 两个字典合并为一个，其中 default_options 字典中的键值对优先级高于 options 字典中的键值对。
        #如果存在相同的键，则后面的字典中的值会覆盖前面的字典中的值。
        options = {**default_options, **options}

        data = {
            "taskId": task_id,
            "options": options
        }
        return self._send_request("api/v1/resumeScan", data)

    def stop_scan(self, task_id):
        """
        停止任务
        :param task_id: 任务ID
        :type task_id: str
        :return: 返回JSON对象，如下：
                 {
                     "success": true,
                     "message": "",
                     "data": {}
                 }
        :rtype: dict
        """
        data = {
            "taskId": task_id
        }
        return self._send_request("api/v1/stopScan", data)

    def get_tasks(self, page=1, size=10, order_by='created_time', order='desc'):
        """
        获取任务列表

        :param page: 页码，默认为 1
        :type page: int
        :param size: 每页数量，默认为 10
        :type size: int
        :param order_by: 排序字段，默认为 created_time
        :type order_by: str
        :param order: 排序方式，默认为 desc
        :type order: str
        :return: 返回任务列表的 JSON 对象
        :rtype: dict
        """
        data = {
            "options": {
                "page": {
                    "page": page,
                    "size": size
                },
                "order": {
                    order_by: order
                }
            }
        }

        return self._send_request("api/v1/getTasks", data)





