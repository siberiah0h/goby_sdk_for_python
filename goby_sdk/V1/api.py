from goby_sdk.V1.lib.asset_page import AssetPage
from goby_sdk.V1.lib.home_page import HomePage
from goby_sdk.V1.lib.vulnerability_management_page import VulnManagementPage
from goby_sdk.V1.lib.report_page import ReportPage
from goby_sdk.V1.lib.config_page import ConfigPage


class Api:
    def __init__(self, url, username, password):
        self.HomePage = HomePage(url, username, password)
        self.AssetPage = AssetPage(url, username, password)
        self.VuleManagePage = VulnManagementPage(url, username, password)
        self.ReportPage = ReportPage(url, username, password)
        self.ConfigPage = ConfigPage(url, username, password)

    # 检测poc列表
    def get_poc_list(self, query="vultype=2", reload_pocs=False,
                     order_by={"vul_nums": "desc", "level": "desc", "host_nums": "desc"}, page=1, size=3000):
        return self.HomePage.get_poc_list(query=query, reload_pocs=reload_pocs, order_by=order_by, page=page, size=size)

    # 启动扫描
    def start_scan(self, task_name, ips, ports="0-65535", black_ips=[], vul_type="0", pocs_hosts={}, options={}):
        return self.HomePage.start_scan(task_name=task_name, ports=ports, ips=ips, black_ips=black_ips,
                                        vul_type=vul_type, pocs_hosts=pocs_hosts, options=options)

    # 重启扫描
    def resume_scan(self, task_id, options={}):
        return self.HomePage.resume_scan(task_id=task_id, options=options)

    # 停止扫描
    def stop_scan(self, task_id):
        return self.HomePage.stop_scan(task_id=task_id)

    # 查询扫描进度
    def get_scan_progress(self, task_id):
        return self.HomePage.get_scan_progress(task_id=task_id)

    # 获取任务列表
    def get_tasks(self, page=1, size=10, order_by='created_time', order='desc'):
        return self.HomePage.get_tasks(page=page, size=size, order_by=order_by, order=order)

    # 查询任务统计数据
    def get_statistics_data(self, task_id):
        return self.AssetPage.get_statistics_data(task_id=task_id)

    # 资产搜索
    def asset_search(self, task_id, query='', page=1, page_size=20,
                     order_by={'vulnerabilities': 'desc', 'assets': 'desc'}):
        return self.AssetPage.asset_search(task_id=task_id, query=query, page=page, page_size=page_size,
                                           order_by=order_by)

    # 获取产品类别
    def get_value_category(self, task_id):
        return self.AssetPage.get_value_category(task_id=task_id)

    # 获取支撑系统
    def get_children_category(self, task_id, parent_category):
        return self.AssetPage.get_children_category(task_id=task_id, parent_category=parent_category)

    # 获取IP详情
    def get_ip_info(self, task_id, ip):
        return self.AssetPage.get_ip_info(task_id=task_id, ip=ip)

    # 获取任务的Web漏洞列表
    def get_web_list(self, task_id, page=1, size=20):
        return self.AssetPage.get_web_list(task_id=task_id, page=page, size=size)

    # 获取漏洞信息
    def get_pocs(self, task_id, query, reload_pocs=False, order_by='vul_nums', order='desc', page=1, page_size=20):
        return self.VuleManagePage.get_pocs(task_id=task_id, query=query, reload_pocs=reload_pocs, order_by=order_by,
                                            order=order, page=page, page_size=page_size)

    # 获取失败的POC列表
    def get_failed_pocs(self):
        return self.VuleManagePage.get_failed_pocs()

    # 获取任务的漏洞统计数据
    def get_vuln_statistics(self, task_id):
        return self.VuleManagePage.get_vuln_statistics(task_id=task_id)

    # 获取任务的漏洞搜索结果
    def get_vulnerability_search(self, task_id, page=1, size=20):
        return self.VuleManagePage.get_vulnerability_search(task_id=task_id, page=page, size=size)

    # 获取POC信息
    def get_poc_info(self, vul_name):
        return self.VuleManagePage.get_poc_info(vul_name=vul_name)

    # 获取指定任务下的IP段信息
    def get_ip_segment(self, task_id, type):
        return self.ReportPage.get_ip_segment(task_id=task_id, segment_type=type)

    # 获取任务的漏洞分析数据
    def get_vul_analysis(self, task_id):
        return self.ReportPage.get_vul_analysis(task_id=task_id)

    # 获取指定任务的资产标签数据
    def get_asset_tags(self, task_id):
        return self.ReportPage.get_asset_tags(task_id=task_id)

    # 配置类：获取可用的网卡列表
    def get_list_adapters(self):
        return self.ConfigPage.get_list_adapters()

    # 配置类：获取系统环境信息
    def get_env_info(self):
        return self.ConfigPage.get_environment_info()

    # 设置系统环境信息
    def set_env_info(self, dns_server, proxy_server):
        return self.ConfigPage.set_environment_info(dns_server=dns_server, proxy_server=proxy_server)
