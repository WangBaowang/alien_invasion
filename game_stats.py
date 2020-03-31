# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/3/29 16:58
# 文件名称: game_stats.py
# 开发工具: PyCharm
import os

class GameStats():
    '''根据游戏的统计信息'''

    def __init__(self, ai_settings):
        '''初始化系统信息'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 在任何情况下都不应该重置最高得分
        f = open('high_score.data', 'r+')
        if not os.path.getsize('high_score.data'):
            f.write(str(0))
        self.high_score = int(f.read())
        f.close()

        # 在任何情况下都不应该重置最高等级
        f = open('high_level.data', 'r+')
        if not os.path.getsize('high_level.data'):
            f.write(str(0))
        self.high_level = int(f.read())
        f.close()

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1