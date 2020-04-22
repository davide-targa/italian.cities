# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s italian.cities -t test_city.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src italian.cities.testing.ITALIAN_CITIES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/italian/cities/tests/robot/test_city.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a City
  Given a logged-in site administrator
    and an add City form
   When I type 'My City' into the title field
    and I submit the form
   Then a City with the title 'My City' has been created

Scenario: As a site administrator I can view a City
  Given a logged-in site administrator
    and a City 'My City'
   When I go to the City view
   Then I can see the City title 'My City'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add City form
  Go To  ${PLONE_URL}/++add++City

a City 'My City'
  Create content  type=City  id=my-city  title=My City

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the City view
  Go To  ${PLONE_URL}/my-city
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a City with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the City title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
