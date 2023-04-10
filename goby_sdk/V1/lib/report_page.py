from goby_sdk.V1.lib.base_page import BasePage


class ReportPage(BasePage):

    def get_ip_segment(self, task_id, segment_type):
        """
        获取指定任务下的IP段信息

        :param task_id: 任务ID
        :type task_id: str
        :param segment_type: IP段类型，0表示所有，1表示已扫描，2表示未扫描
        :type segment_type: str
        :return: 返回IP段信息的JSON对象
        :rtype: dict
        """
        # 组装请求数据
        data = {
            "taskId": task_id,
            "type": segment_type
        }
        # 发送请求并返回响应结果
        return self._send_request("api/v1/ipSegment", data)

    def get_vul_analysis(self, task_id):
        """
        获取任务的漏洞分析数据

        :param task_id: 任务ID
        :type task_id: str
        :return: 返回漏洞分析数据的JSON对象
        :rtype: dict
        """
        # 组装请求数据
        data = {
            "taskId": task_id
        }
        # 发送请求并返回响应结果
        return self._send_request("api/v1/getVulAnalysis", data)

    def get_asset_tags(self, task_id):
        """
        获取指定任务的资产标签数据

        :param task_id: 任务ID
        :type task_id: str
        :return: 返回资产标签数据的JSON对象
        :rtype: dict
        """
        data = {"taskId": task_id}
        return self._send_request("api/v1/assetTags", data)
