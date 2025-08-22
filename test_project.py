from project import AlienInvasion, Bullet, Alien
import pygame

def test_check_play_button():
    """Test the _check_play_button method."""

    ai = AlienInvasion()
    ai.stats.game_active = False
    mouse_pos = ai.play_button.rect.center
    ai._check_play_button(mouse_pos)
    assert ai.stats.game_active is True
    assert not pygame.mouse.get_visible()

def test_fire_bullet():
    """Test the _fire_bullet method."""

    ai = AlienInvasion()
    ai.bullets.empty()
    ai._fire_bullet()
    assert len(ai.bullets) == 1
    ai._fire_bullet()
    ai._fire_bullet()
    assert len(ai.bullets) == ai.settings.bullets_allowed

def test_ship_hit():
    """Test the _ship_hit method."""

    ai = AlienInvasion()
    ai.stats.ships_left = 3
    ai._ship_hit()
    assert ai.stats.ships_left == 2
    ai.stats.ships_left = 1
    ai._ship_hit()
    assert ai.stats.game_active is False

def test_create_fleet():
    """Test the _create_fleet method."""

    ai = AlienInvasion()
    ai.aliens.empty()
    ai._create_fleet()
    assert len(ai.aliens) > 0