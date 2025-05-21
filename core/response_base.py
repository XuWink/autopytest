'''
格式化http返回的结果
'''
import requests
from typing import Optional, Dict, Any
from dataclasses import dataclass
from common.logger import logger

@dataclass
class ResultBase:
    """极致精简的结果基类"""
    success: bool = False
    response: Optional[requests.Response] = None  # 唯一数据存储源
 
    @property
    def response_json(self) -> Optional[Dict[str, Any]]:
        """动态获取解析后的数据"""
        if self.response is not None:
            try:
                return self.response.json()
            except ValueError:  # 捕获 JSON 解析错误
                logger.error("Failed to parse response JSON")
        return None
 
    @property
    def msg(self) -> str:
        """动态获取消息"""
        return self.response_json.get("msg", "") if self.response_json else ""
    
    @property
    def data(self) -> Any:  # 改为 Any 类型，因为 data 可以是任意类型
        """动态获取数据"""
        return self.response_json.get("data") if self.response_json else None