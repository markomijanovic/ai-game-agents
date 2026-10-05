import math
import random
import time


class Agent:
    ident = 0

    def __init__(self):
        self.id = Agent.ident
        Agent.ident += 1

    def get_chosen_action(self, state, max_depth):
        pass


class RandomAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        return actions[random.randint(0, len(actions) - 1)]

class GreedyAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        best_score, best_action = None, None
        for action in actions:
            new_state = state.generate_successor_state(action)
            score = new_state.get_score(state.get_on_move_chr())
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action

class MaxNAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        me = state.get_on_move_ord()
        n_players = state.get_num_of_players()
        kinds = [chr(ord('A') + i) for i in range(n_players)]

        def eval_vector(s):
            # vektor skorova u redosledu A, B, C, D... (dužine n_players)
            return tuple(s.get_score(k) for k in kinds)

        def maxn(s, depth):
            # ako smo na listu (cilj ili dubina), vrati trenutne skorove
            if depth <= 0 or s.is_goal_state():
                return eval_vector(s)

            player = s.get_on_move_ord()
            best_val = None

            actions = s.get_legal_actions()
            for a in actions:
                child = s.generate_successor_state(a)
                cand = maxn(child, depth - 1)
                if best_val is None or cand[player] > best_val[player]:
                    best_val = cand

            # ako nema legalnih poteza, evaluiraj trenutno stanje
            return best_val if best_val is not None else eval_vector(s)

        # izbor poteza na korenu – maksimizujemo komponentu za trenutnog igrača
        best_action, best_me_val = None, float("-inf")
        for a in state.get_legal_actions():
            child = state.generate_successor_state(a)
            val_vec = maxn(child, max_depth - 1)
            if val_vec[me] > best_me_val:
                best_me_val = val_vec[me]
                best_action = a

        return best_action

class MinimaxAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        max_player = state.get_on_move_chr()
        min_player = 'B' if max_player == 'A' else 'A'   # pretpostavka: A,B

        def state_evaluation(st):
            return st.get_score(max_player) - st.get_score(min_player)

        def minimax_value(s, depth):
            if depth <= 0 or s.is_goal_state():
                return state_evaluation(s)

            on_move = s.get_on_move_chr()
            actions = s.get_legal_actions()
            if not actions:
                return state_evaluation(s)

            if on_move == max_player:  # MAX potez
                best = float("-inf")
                for a in actions:
                    child = s.generate_successor_state(a)
                    best = max(best, minimax_value(child, depth - 1))
                return best
            else:  # MIN potez
                best = float("inf")
                for a in actions:
                    child = s.generate_successor_state(a)
                    best = min(best, minimax_value(child, depth - 1))
                return best

        best_action, best_val = None, float("-inf")
        for a in state.get_legal_actions():
            v = minimax_value(state.generate_successor_state(a), max_depth - 1)
            if v > best_val:
                best_val, best_action = v, a
        return best_action

class MinimaxABAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        max_player = state.get_on_move_chr()
        min_player = 'B' if max_player == 'A' else 'A'

        def state_evaluation(st):
            return st.get_score(max_player) - st.get_score(min_player)

        def ab_value(s, depth, alpha, beta):
            if depth <= 0 or s.is_goal_state():
                return state_evaluation(s)

            on_move = s.get_on_move_chr()
            actions = s.get_legal_actions()
            if not actions:
                return state_evaluation(s)

            if on_move == max_player:  # MAX potez
                v = float("-inf")
                for a in actions:
                    v = max(v, ab_value(s.generate_successor_state(a), depth - 1, alpha, beta))
                    alpha = max(alpha, v)
                    if alpha >= beta:
                        break  # sečenje
                return v
            else:  # MIN potez
                v = float("inf")
                for a in actions:
                    v = min(v, ab_value(s.generate_successor_state(a), depth - 1, alpha, beta))
                    beta = min(beta, v)
                    if alpha >= beta:
                        break  # sečenje
                return v

        best_action, best_val = None, float("-inf")
        alpha, beta = float("-inf"), float("inf")
        for a in state.get_legal_actions():
            v = ab_value(state.generate_successor_state(a), max_depth - 1, alpha, beta)
            if v > best_val:
                best_val, best_action = v, a
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break
        return best_action
