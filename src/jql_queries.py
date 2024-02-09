from src.config import PROJECTS_KEY

last_year_and_this_year = 'created >= startOfYear(-1) AND created <= endOfYear()'

multiple_projects = 'project IN ({})'.format(', '.join(['"{}"'.format(key) for key in PROJECTS_KEY]))

multiple_projects_last_year_and_this_year = '{} AND {}'.format(multiple_projects, last_year_and_this_year)

unresolved_high_priority = 'priority = High AND resolution is EMPTY'.format(
                            ', '.join(['"{}"'.format(key) for key in PROJECTS_KEY])
                            )

multiple_projects_unresolved_high_priority = '{} AND {}'.format(multiple_projects, unresolved_high_priority)

in_progress_assigned_to_user = 'status = "In Progress" AND assignee is not EMPTY'.format(
                            ', '.join(['"{}"'.format(key) for key in PROJECTS_KEY])
                            )

multiple_projects_in_progress_assigned_to_user = '{} AND {}'.format(multiple_projects, in_progress_assigned_to_user)

QUERIES = [
    multiple_projects,
    last_year_and_this_year,
    unresolved_high_priority,
    in_progress_assigned_to_user,
    multiple_projects_last_year_and_this_year,
    multiple_projects_unresolved_high_priority,
    multiple_projects_in_progress_assigned_to_user
]
