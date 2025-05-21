'''
工具类，用于读取ini文件，json文件，yaml文件为字典
'''
import yaml
import json
from configparser import ConfigParser
from typing import Dict, Any
from pathlib import Path
from common.logger import logger


class MyConfigParser(ConfigParser):
    """自定义ConfigParser类，禁用键名小写转换"""
    def optionxform(self, option: str) -> str:
        """重写optionxform方法，保持键名原样"""
        return option


class FileLoader:
    """文件加载器，支持 YAML、JSON 和 INI 格式文件的读取"""
    
    @staticmethod
    def _check_file_exists(file_path: str) -> None:
        """检查文件是否存在，不存在则抛出异常"""
        if not Path(file_path).exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")
 
    @staticmethod
    def load_yaml(file_path: str) -> Dict[str, Any]:
        """
        加载 YAML 文件
        :param file_path: 文件路径
        :return: 解析后的字典数据
        :raises FileNotFoundError: 文件不存在时抛出
        :raises yaml.YAMLError: YAML 解析错误时抛出
        """
        logger.info(f"加载 YAML 文件: {file_path}")
        try:
            FileLoader._check_file_exists(file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
            logger.debug(f"读取到 YAML 数据: {data}")
            return data
        except yaml.YAMLError as e:
            logger.error(f"解析 YAML 文件失败: {file_path}, 错误: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"加载 YAML 文件失败: {file_path}, 错误: {str(e)}")
            raise
    
    @staticmethod
    def load_json(file_path: str) -> Dict[str, Any]:
        """
        加载 JSON 文件
        :param file_path: 文件路径
        :return: 解析后的字典数据
        :raises FileNotFoundError: 文件不存在时抛出
        :raises json.JSONDecodeError: JSON 解析错误时抛出
        """
        logger.info(f"加载 JSON 文件: {file_path}")
        try:
            FileLoader._check_file_exists(file_path)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.debug(f"读取到 JSON 数据: {data}")
            return data
        except json.JSONDecodeError as e:
            logger.error(f"解析 JSON 文件失败: {file_path}, 错误: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"加载 JSON 文件失败: {file_path}, 错误: {str(e)}")
            raise
    
    @staticmethod
    def load_ini(file_path: str) -> Dict[str, Any]:
        """
        加载 INI 文件
        :param file_path: 文件路径
        :return: 解析后的字典数据
        :raises FileNotFoundError: 文件不存在时抛出
        """
        logger.info(f"加载 INI 文件: {file_path}")
        try:
            FileLoader._check_file_exists(file_path)
            
            config = MyConfigParser()
            config.read(file_path, encoding='UTF-8')
            data = {section: dict(config.items(section)) for section in config.sections()}
            logger.debug(f"读取到 INI 数据: {data}")
            return data
        except Exception as e:
            logger.error(f"加载 INI 文件失败: {file_path}, 错误: {str(e)}")
            raise