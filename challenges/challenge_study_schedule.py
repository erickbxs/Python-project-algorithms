def study_schedule(permanence_periods, target_time):
    if not permanence_periods or target_time is None:
        return None

    count = 0
    for entry, exit_time in permanence_periods:
        if (
            isinstance(entry, int)
            and isinstance(exit_time, int)
            and entry <= exit_time
        ):
            if entry <= target_time <= exit_time:
                count += 1
        else:
            return None

    return count
