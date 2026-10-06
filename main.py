from cli import parse_args

def main():
    args = parse_args()
    import pygame
    import config
    from game import Game

    names = args.agents.split(',')
    if len(names) > config.MAX_PLAYERS:
        raise ValueError('Too many agents!')
    config.DEBUG = args.debug
    try:
        Game(names, args.map, args.rounds, args.elapsed, args.depth).run()
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
