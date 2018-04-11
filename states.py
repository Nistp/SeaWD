

article_completion_states = {
    'DRAFT',
    'STAGED',
    'PUBLISHED',
    'MODIFIED' # as in RE-PUBLISHED / UPDATED
    }


article_online_states = {
    'ONLINE',
    'STAGED', # put staged here instead of completion states?
    'OFFLINE'
    }

#orthogonal? statecharts
#article state = completion state * online state

transitions = {
    'edit',
    'stage',
    'publish',
    }

incidence = {
    'DRAFT': {
     'edit': 'DRAFT',
     'stage': 'STAGED',
    },
    'STAGED': {
     'edit': 'DRAFT',
     'stage': 'STAGED',
     'publish': 'PUBLISHED',
    },

    'PUBLISHED': {
     'edit': 'MODIFIED',
     'stage': 'STAGED',
     'publish': 'PUBLISHED',
    },

    'MODIFIED': {
     'edit': 'MODIFIED',
     'stage': 'STAGED',
    }

    }

#i think we need orthgonal states
#state = ('PUBLISHED', 'ONLINE') # hashable?
#
#new_state = transition(state)['action']
#


print(incidence)
print(incidence['DRAFT'])
print(incidence['DRAFT']['edit'])
print(incidence['DRAFT']['stage'])

initial_state = 'DRAFT'
print('created an article. initial state is {initial_state}')

action = 'edit'
state = incidence[initial_state][action]
print(f'performed {action}. the article is {state}')

action = 'edit'
state = incidence[state][action]
print(f'performed {action}. the article is {state}')


action = 'stage'
state = incidence[state][action]
print(f'performed {action}. the article is {state}')


action = 'publish'
state = incidence[state][action]
print(f'performed {action}. the article is {state}')


action = 'edit'
state = incidence[state][action]
print(f'performed {action}. the article is {state}')
