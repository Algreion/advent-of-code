# I might stop at day 10, I'm quite at this time.
from collections import deque
import heapq

def day9_solve1(input: str) -> int: # Ans: 6385338159127
    blocks = deque(enumerate(int(n) for n in input[::2]))
    space = deque(int(n) for n in input[1::2])
    res = []
    while blocks:
        new_block = blocks.popleft()
        res.append(new_block)
        if space:
            new_gap = space.popleft()
            while blocks and new_gap:
                id, size = blocks.pop()
                if size <= new_gap:
                    res.append((id, size))
                    new_gap -= size
                else:
                    res.append((id, new_gap))
                    blocks.append((id, size-new_gap))
                    new_gap = 0
    checksum = 0
    i = 0
    for id, size in res:
        checksum += id*size*(2*i + size-1)//2
        i += size
    return checksum

def day9_solve2(input: str) -> int: # Ans: 6415163624282
    is_block = True
    blocks = []
    gaps = [[] for _ in range(10)]
    pos, id = 0, 0
    for d in input:
        d = int(d)
        if is_block:
            blocks.append([pos, id, d])
            id += 1
        else:
            heapq.heappush(gaps[d], pos)
        pos += d
        is_block = not is_block
    checksum = 0
    for b in range(len(blocks))[::-1]:
        pos, id, size = blocks[b]
        best = pos
        candidates = [(heapq.heappop(gaps[i]), i) for i in range(10) if gaps[i] and i>=size]
        if candidates:
            gpos, glen = min(candidates)
            if gpos < pos:
                best = gpos
                candidates.remove((gpos, glen))
                heapq.heappush(gaps[glen-size], gpos+size)
            for gpos, glen in candidates:
                heapq.heappush(gaps[glen], gpos)
            blocks[b][0] = best
        checksum += id*size*(2*best + size-1)//2
    return checksum
