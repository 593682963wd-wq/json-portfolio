"""作者：Wangyuan；日期：2026-10-29；职责：显式工具注册表统计。"""
import registry

def run(payload):
    if not isinstance(payload,dict):raise TypeError('输入须对象')
    tools=payload.get('tools',[])
    if not isinstance(tools,list) or any(not isinstance(x,dict) for x in tools):raise ValueError('工具须对象数组')
    return registry._registry_stats(tools)
