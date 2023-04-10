from goby_sdk.V1.lib.base_page import BasePage

class AssetPage(BasePage):
    def get_statistics_data(self, task_id):
        """
        获取任务的统计数据
        :param task_id: 任务ID
        :type task_id: str
        :return: 返回统计数据的JSON对象
        :rtype: dict
        """
        data = {
            "taskId": task_id
        }
        return self._send_request("api/v1/getStatisticsData", data)

    def asset_search(self, task_id, query='', page=1, page_size=20,
                     order_by={'vulnerabilities': 'desc', 'assets': 'desc'}):
        """
        根据查询条件搜索资产
        :param task_id: 任务ID
        :type task_id: str
        :param query: 查询条件，字符串形式，默认为空字符串
        :type query: str
        :param page: 分页页码，默认为1
        :type page: int
        :param page_size: 分页大小，默认为20
        :type page_size: int
        :param order_by: 排序字段和排序方式，默认为 {'vulnerabilities': 'desc', 'assets': 'desc'}
        :type order_by: dict
        :return: 返回搜索结果的JSON对象
        :rtype: dict
        """
        data = {
            "query": f"taskId=\"{task_id}\" && ({query})",
            "options": {
                "order": order_by,
                "page": {
                    "page": page,
                    "size": page_size
                }
            }
        }
        options = {'order': {'vulnerabilities': 'desc', 'assets': 'desc'}, 'page': {'page': 1, 'size': 20}}
        options = {**options, **order_by, 'page': {'page': page, 'size': page_size}}
        data['options'] = options

        return self._send_request("api/v1/assetSearch", data)

    def get_value_category(self, task_id):
        """
           获取任务值的分类
           :param task_id: 任务ID
           :type task_id: str
           :return: 返回任务列表的 JSON 对象
           :rtype: dict
           """
        data = {
            "taskId": task_id
        }
        return self._send_request("api/v1/getValueCategory", data)

    def get_children_category(self, task_id, parent_category):
        """
        获取子类别列表
        :param task_id: 任务ID
        :type task_id: str
        :param parent_category: 父类别
        :type parent_category: str
        :return: 返回JSON对象
        :rtype: dict
        """
        data = {
            "query": f"taskId=\"{task_id}\" && parent_category=\"{parent_category}\""
        }
        return self._send_request("api/v1/getChildrenCategory", data)

    def get_ip_info(self, task_id, ip):
        """
        获取IP信息
        :param task_id: 任务ID
        :type task_id: str
        :param ip: IP地址
        :type ip: str
        :return: 返回JSON对象
        :rtype: dict
        """
        data = {
            "taskId": task_id,
            "ip": ip
        }
        return self._send_request("api/v1/getIPInfo", data)

    def get_web_list(self, task_id, page=1, size=20):
        """
         获取任务的Web漏洞列表

         :param task_id: 任务ID
         :type task_id: str
         :param page: 页码，默认为1
         :type page: int
         :param size: 每页显示的记录数，默认为20
         :type size: int
         :return: 返回Web漏洞列表的JSON对象
         :rtype: dict
         """
        # 组装请求数据
        data = {
            "taskId": task_id,
            "options": {
                "page": {"page": page, "size": size}
            }
        }
        # 发送请求并返回响应结果
        return self._send_request("api/v1/getWebList", data)
