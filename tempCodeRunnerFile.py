                if abs(pong.left - p1rect.right) < collision_tolerance:
                    pong_velocity_x *= -1
                if abs(pong.right - p2rect.left) < collision_tolerance:
                    pong_velocity_x *= -1