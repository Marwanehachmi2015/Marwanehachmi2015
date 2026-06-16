"""
نظام تسجيل الأحداث لروبوت التداول
Logging system for trading bot
"""

import logging
import os
from datetime import datetime
from pathlib import Path

# إنشاء مجلد السجلات
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

def setup_logger(name, log_level=logging.INFO):
    """
    إعداد نظام التسجيل
    Setup logging system
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # تنسيق السجل
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # معالج الملف
    log_file = log_dir / f'{name}_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    
    # معالج Console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # إضافة المعالجات
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# إنشاء logger رئيسي
main_logger = setup_logger('gold_trading_bot')
