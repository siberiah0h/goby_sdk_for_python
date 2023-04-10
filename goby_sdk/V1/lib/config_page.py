from goby_sdk.V1.lib.base_page import BasePage


class ConfigPage(BasePage):

    def get_list_adapters(self):
        """
        获取可用的网卡列表

        :return: 返回网卡列表的JSON对象
        :rtype: dict
        """
        return self._send_get_request("api/v1/listAdapters")

    def get_environment_info(self):
        """
        获取系统环境信息

        :param field: 需要获取的字段，多个字段用逗号分隔，默认获取全部
        :type field: str
        :return: 返回系统环境信息的JSON对象
        :rtype: dict
        """
        # 查询参数
        field = 'chromePath,dataIntegrity,datadir,dir,midKey,proxyServer,userRuleSize,vulVersion,licenseInfo,gid,key,godserver'
        params = {
            'field': field
        }
        # 发送GET请求
        return self._send_get_request('api/v1/getEnvi', params=params)

    def set_environment_info(self, dns_server, proxy_server):
        """
        设置系统环境信息
        :param dns_server: DNS 服务器地址和端口，例如 "8.8.8.8:53"
        :type dns_server: str
        :param proxy_server: 代理服务器地址和端口，例如 "http://192.168.61.41:1080"
        :type proxy_server: str
        :return: 返回设置结果的 JSON 对象
        :rtype: dict
        """
        # 组装请求参数
        data = {
            "dnsServer": dns_server,
            "proxyServer": proxy_server
        }
        # 发送请求并返回响应结果
        return self._send_request("api/v1/setEnvi", data)
