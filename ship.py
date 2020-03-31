# -*- coding:utf-8 -*-
# 开发者: baowang
# 开发时间: 2020/3/28 21:52
# 文件名称: ship.py
# 开发工具: PyCharm
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        super().__init__()
        self.screen = screen  # 将飞船绘制到哪里
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('F:/Files/Python/tools/alien_invasion/images/ship.png')
        self.rect = self.image.get_rect()  # 处理rect 对象时，可使用矩形四角和中心的 x 和 y 坐标。可通过设置这些值来指定矩形的位置
        self.screen_rect = screen.get_rect()

        # 将每一艘新飞机放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False  # 右移
        self.moving_left = False   # 左移
        self.moving_up = False     # 上移
        self.moving_down = False   # 下移

    def update(self, sb):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > sb.level_rect.bottom:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom