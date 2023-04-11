# GOBY SDK for Python

GOBY SDK for Python是一个非官方版本的GOBY SDK，基于 goby-x64-2.4.5-Community 进行开发。

该SDK旨在解决企业系统快速集成GOBY扫描引擎的问题。

详细SDK文档请访问： <https://www.exp-9.com/category-20.html> 或 <https://github.com/siberiah0h/goby_sdk_for_python>。

## API接口列表

以下是一些API接口及其含义的列表：

*   `get_poc_list` 函数：获取POC列表
*   `start_scan` 函数：开始扫描
*   `resume_scan` 函数：恢复扫描
*   `stop_scan` 函数：停止扫描
*   `get_scan_progress` 函数：获取扫描进度
*   `get_tasks` 函数：获取任务
*   `get_statistics_data` 函数：获取统计数据
*   `asset_search` 函数：资产搜索
*   `get_value_category` 函数：获取值分类
*   `get_children_category` 函数：获取子分类
*   `get_ip_info` 函数：获取IP信息
*   `get_web_list` 函数：获取Web列表
*   `get_pocs` 函数：获取POCS
*   `get_failed_pocs` 函数：获取失败的POCS
*   `get_vuin_statistics` 函数：获取漏洞统计信息
*   `get_vulnerability_search` 函数：获取漏洞搜索结果
*   `get_poc_info` 函数：获取POC信息
*   `get_ip_segment` 函数：获取IP段
*   `get_vulanalysis` 函数：获取漏洞分析结果
*   `get_asset_tags` 函数：获取资产标签
*   `get_env_info` 函数：获取环境信息
*   `set_envinfo` 函数：设置环境信息

这些API接口涵盖了漏洞扫描、统计数据、资产搜索等多方面的操作。用户可以根据实际需求选择相应的API接口进行调用。

更多详情和调用方法请访问 <https://www.exp-9.com/category-20.html>。

## 安装方法

使用以下命令安装GOBY SDK for Python：

`pip install goby-sdk`
