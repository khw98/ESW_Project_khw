from settings import *
from src.object_controller import ObjectController
from PIL import Image
import time, os

# 객체 정보 정의
OBJECT_INFO = {
    'player': {
        'width': 51,
        'height': 51,
        'size': (51, 51),
        'path': os.path.join(IMAGE_PATH, 'player.png'),
        'speed': (13, 13),
        'role': 'fighter-plane',
        'missile-name': 'missile0',
        'hp': 1
    },
    'enemy1': {
        'width': 47,
        'height': 47,
        'size': (47, 47),
        'path': os.path.join(IMAGE_PATH, 'enemy1.png'),
        'speed': (0, 4),
        'role': 'fighter-plane',
        'stlye': 'past',
        'pattern': 'basic',
        'missile_speed': (0, 2),
        'attack-cycle': 2,
        'missile-name': 'missile1',
        'hp': 1
    },
    'enemy2': {
        'width': 47,
        'height': 47,
        'size': (47, 47),
        'path': os.path.join(IMAGE_PATH, 'enemy2.png'),
        'speed': (3, 3),
        'role': 'fighter-plane',
        'stlye': 'past',
        'pattern': 'basic',
        'missile_speed': (0, 2),
        'attack-cycle': 2,
        'missile-name': 'missile2',
        'hp': 1
    },
    'enemy2-2': {
        'width': 47,
        'height': 47,
        'size': (47, 47),
        'path': os.path.join(IMAGE_PATH, 'enemy2.png'),
        'speed': (-3, 3),
        'role': 'fighter-plane',
        'stlye': 'past',
        'pattern': 'basic',
        'missile_speed': (0, 2),
        'attack-cycle': 2,
        'missile-name': 'missile2',
        'hp': 1
    },
    'enemy3': {
        'width': 77,
        'height': 77,
        'size': (77, 77),
        'path': os.path.join(IMAGE_PATH, 'enemy3.png'),
        'speed': (1, 1),
        'role': 'fighter-plane',
        'stlye': 'basic',
        'pattern': 'spray',
        'missile_speed': ((-2, 3), (-1, 4), (0, 4), (1, 4), (2, 3)),
        'attack-cycle': 3,
        'missile-name': 'missile3',
        'hp': 15
    },
    'boss': {
        'width': 77,
        'height': 77,
        'size': (77, 77),
        'path': os.path.join(IMAGE_PATH, 'boss.png'),
        'speed': (1, 1),
        'role': 'fighter-plane',
        'stlye': 'basic',
        'pattern': 'spray',
        'missile_speed': ((-2, 5), (-2, 4), (-2, 3), (-2, 2), (2, 2), (2, 3), (2, 4), (2, 5)),
        'attack-cycle': 3,
        'missile-name': 'missile4',
        'hp': 15
    },
    'missile0': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile0.png'),
        'speed': (0, -9),
        'role': 'missile',
        'damage': 1
    },
    'missile1': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile1.png'),
        'speed': (0, 9),
        'role': 'missile',
        'damage': 1
    },
    'missile2': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile2.png'),
        'speed': (0, 9),
        'role': 'missile',
        'damage': 1
    },
    'missile3': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile3.png'),
        'speed': (5, 5),
        'role': 'missile',
        'damage': 1
    },
    'missile4': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile4.png'),
        'speed': (0, 2),
        'role': 'missile',
        'pattern': 'spray',
        'damage': 1
    },
    'missile5': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile5.png'),
        'speed': (0, 2),
        'role': 'missile',
        'damage': 1
    },
    'missile6': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile6.png'),
        'speed': (0, 2),
        'role': 'missile',
        'damage': 1
    },
    'missile7': {
        'width': 13,
        'height': 13,
        'size': (13, 13),
        'path': os.path.join(IMAGE_PATH, 'missile7.png'),
        'speed': (0, 2),
        'role': 'missile',
        'damage': 1
    },
    'effect-boom1': {
        'width': 61,
        'height': 61,
        'size': (61, 61),
        'path': os.path.join(IMAGE_PATH, 'effect-boom2.png'),
        'speed': (0, 0),
        'team': 'none',
        'role': 'effect',
    }
}


# 기본 게임 객체 클래스
class GameObject:
    def __init__(self, obj_coord, name, team, speed):
        # 객체 초기화
        self.__name = name
        self.__team = team
        self.__speed = OBJECT_INFO[self.name]['speed'] if speed == None else speed
        self.__role = OBJECT_INFO[self.name]['role']
        self.__width = OBJECT_INFO[self.name]['width']
        self.__height = OBJECT_INFO[self.name]['height']
        self.__image = Image.open(OBJECT_INFO[self.name]['path']).resize(OBJECT_INFO[self.name]['size'])
        self.__obj_coord = obj_coord
        self.__image_coord = self.image_coord
        self.__obj_id = ObjectController.enroll(self)

    # 객체 속성 정의
    @property
    def name(self):
        return self.__name

    @property
    def team(self):
        return self.__team

    @property
    def role(self):
        return self.__role

    @property
    def image(self):
        return self.__image

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def obj_coord(self):
        return self.__obj_coord

    def _set_obj_coord(self, new_coord):
        self.__obj_coord = new_coord

    @property
    def speed(self):
        return self.__speed

    def _reverse_speed(self, option='width'):
        if option == 'width':
            self.__speed = (-self.__speed[0], self.__speed[1])
        else:
            self.__speed = (self.__speed[0], -self.__speed[1])

    @property
    def image_coord(self):
        # 이미지 좌표 계산
        self.__image_coord = (self.obj_coord[0] - self.width // 2, self.obj_coord[1] - self.height // 2,
                              self.obj_coord[0] + self.width // 2 + 1, self.obj_coord[1] + self.height // 2 + 1)
        return self.__image_coord

    @property
    def obj_id(self):
        return self.__obj_id

    def move(self):
        # 객체 이동
        self._set_obj_coord((self.obj_coord[0] + self.speed[0], self.obj_coord[1] + self.speed[1]))


# 플레이어 클래스
class Player(GameObject):
    def __init__(self, obj_coord, name='player', team='player', role='fighter-plane', speed=None):
        super().__init__(obj_coord, name, team, speed)
        self.__hp = OBJECT_INFO[self.name]['hp']
        self.__kill_point = 0

    @property
    def hp(self):
        return self.__hp

    @property
    def kill_point(self):
        return self.__kill_point

    def _add_kill_point(self):
        self.__kill_point += 1

    def _be_attacked(self, missile):
        self.__hp -= missile.damage
        if self.__hp <= 0:
            BoomEffect(self.obj_coord)

    def shoot(self):
        # 플레이어 미사일 발사
        missile_coord = (self.obj_coord[0], self.obj_coord[1] - self.height // 2 - 5)
        Missile(missile_coord, OBJECT_INFO[self.name]['missile-name'], self.team)

    def move(self, key):
        # 키 입력에 따른 이동
        if key == 'L':
            self._set_obj_coord((self.obj_coord[0] - self.speed[0], self.obj_coord[1]))
        elif key == 'R':
            self._set_obj_coord((self.obj_coord[0] + self.speed[0], self.obj_coord[1]))
        elif key == 'U':
            self._set_obj_coord((self.obj_coord[0], self.obj_coord[1] - self.speed[1]))
        elif key == 'D':
            self._set_obj_coord((self.obj_coord[0], self.obj_coord[1] + self.speed[1]))


# 적 클래스
class Enemy(GameObject):
    def __init__(self, obj_coord, name='enemy1', team='enemy', role='fighter-plane', speed=None):
        super().__init__(obj_coord, name, team, speed)
        self.__prev_attack_time = time.time()
        self.__attack_cycle = OBJECT_INFO[self.name]['attack-cycle']
        self.__hp = OBJECT_INFO[self.name]['hp']
        self.__stlye = OBJECT_INFO[self.name]['stlye']
        self.__pattern = OBJECT_INFO[self.name]['pattern']

    @property
    def hp(self):
        return self.__hp

    def _be_attacked(self, missile):
        self.__hp -= missile.damage
        if self.__hp <= 0:
            BoomEffect(self.obj_coord)

    def move(self):
        # 적 이동 패턴 처리
        self._set_obj_coord((self.obj_coord[0] + self.speed[0], self.obj_coord[1] + self.speed[1]))
        if self.__stlye == 'basic':
            if self.obj_coord[1] <= 0 or self.obj_coord[1] >= SCREEN_HEIGHT // 2:
                self._reverse_speed('height')
            if self.obj_coord[0] <= 1 or self.obj_coord[0] >= SCREEN_WIDTH - 1:
                self._reverse_speed('width')
            self._set_obj_coord((self.obj_coord[0] + self.speed[0], self.obj_coord[1] + self.speed[1]))

    def shoot(self):
        # 적 미사일 발사
        if time.time() - self.__prev_attack_time >= self.__attack_cycle:
            if self.__pattern == 'spray':
                missile_speed = OBJECT_INFO[self.name]['missile_speed']
                for s in missile_speed:
                    Missile((self.obj_coord[0], self.obj_coord[1] + self.height // 2 + 5),
                            OBJECT_INFO[self.name]['missile-name'], speed=s)
                self.__prev_attack_time = time.time()
            else:
                Missile((self.obj_coord[0], self.obj_coord[1] + self.height // 2 + 5),
                        OBJECT_INFO[self.name]['missile-name'])
                self.__prev_attack_time = time.time()


# 미사일 클래스
class Missile(GameObject):
    def __init__(self, obj_coord, name='missile1', team='enemy', role='missile', speed=None):
        super().__init__(obj_coord, name, team, speed)
        self.__damage = OBJECT_INFO[self.name]['damage']

    @property
    def damage(self):
        return self.__damage


# 폭발 효과 클래스
class BoomEffect(GameObject):
    def __init__(self, obj_coord, name='effect-boom1', team='none', role='effect', speed=None):
        super().__init__(obj_coord, name, team, speed)