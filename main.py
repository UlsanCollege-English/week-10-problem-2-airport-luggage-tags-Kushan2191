"""
HW02 — Airport Luggage Tags (Open Addressing with Delete)
Implement linear probing with EMPTY and DELETED markers.
"""

# Step 4: create unique marker objects
EMPTY = object()
DELETED = object()

def make_table_open(m):
    """Return a table of length m filled with EMPTY markers."""
    return [EMPTY] * m

def _find_slot_for_insert(t, key):
    """Return index to insert/overwrite (may return DELETED slot). Return None if full."""
    m = len(t)
    i = hash(key) % m
    start = i
    first_deleted = None
    while True:
        slot = t[i]
        if slot is EMPTY:
            return i if first_deleted is None else first_deleted
        if slot is DELETED:
            if first_deleted is None:
                first_deleted = i
        elif isinstance(slot, tuple) and slot[0] == key:
            return i
        i = (i + 1) % m
        if i == start:
            return first_deleted

def _find_slot_for_search(t, key):
    """Return index where key is found; else None. DELETED does not stop search."""
    m = len(t)
    i = hash(key) % m
    start = i
    while True:
        slot = t[i]
        if slot is EMPTY:
            return None
        if slot is not DELETED and isinstance(slot, tuple) and slot[0] == key:
            return i
        i = (i + 1) % m
        if i == start:
            return None

def put_open(t, key, value):
    """Insert or overwrite (key, value). Return True on success, False if table is full."""
    idx = _find_slot_for_insert(t, key)
    if idx is None:
        return False
    t[idx] = (key, value)
    return True

def get_open(t, key):
    """Return value for key or None if not present."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return None
    return t[idx][1]

def delete_open(t, key):
    """Delete key if present. Return True if removed, else False."""
    idx = _find_slot_for_search(t, key)
    if idx is None:
        return False
    t[idx] = DELETED
    return True

if __name__ == "__main__":
    # Optional manual checks (not graded)
    pass
