#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Fri 17 Nov 2017 09:48:04 AM CST
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'stopsignaltask_keyFinalnondynamic'  # from the Builder filename that created this script
expInfo = {u'Gender(m/f/o)': u'', u'Age': u'', u'UIN': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['UIN'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "hand"
handClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='Are you left- or right-handed?',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'left', u'right'], tickHeight=-1)

# Initialize components for Routine "lang"
langClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Is English your first language?',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'Yes', u'No'], tickHeight=-1)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='In the following experiment you will see white dots moving left or right. \nYour task is to indicate which direction they are moving by pressing "<-" or "->" key on the keyboard.\nOn some trials you will hear the "BEEP" signal. Please do not press anything if you hear this signal.\nPress SPACE to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='+',    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
dots = visual.DotStim(win=win, name='dots',
    nDots=100, dotSize=5,
    speed=0.05, dir=1.0, coherence=1.0,
    fieldPos=(0.0, 0.0), fieldSize=0.85,fieldShape='circle',
    signalDots='same', noiseDots='direction',dotLife=3,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=1,    depth=-1.0)
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

import numpy as np

#msg variable just needs some value at start
msg =''
scores = 0
feedbackmsg = visual.TextStim(win=win, ori=0, name='feedbackmsg',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='On the following screen you will see items concerning behaviors or problems sometimes experienced by adults. \nRead each item carefully and decide how much or how frequently each item describes you recently. \nIndicate your response by choosing the option that corresponds to your choice. \nUse the following scale: 0 = Not at all, never; 1 = Just a little, once in a while; 2 = Pretty much, often; and 3 = Very much, very frequently.\nPress SPACE to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "caars"
caarsClock = core.Clock()
caars_quest = visual.TextStim(win=win, ori=0, name='caars_quest',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
caars_desc = visual.TextStim(win=win, ori=0, name='caars_desc',
    text='0 = Not at all, Never\n1 = Just a little, Once in a while\n2 = Pretty much, Often\n3 = Very much, Very frequently',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
caars_rating = visual.RatingScale(win=win, name='caars_rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'0', u'1', u'2', u'3'], tickHeight=-1)

# Initialize components for Routine "instr_bdefs"
instr_bdefsClock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='How often do you experience each of these problems?\nChoose the number that best describes your behavior DURING THE PAST 6 MONTHS\n\n1 - Never or rarely\n2 - Sometimes\n3 - Often\n4 - Very often\n\nPress SPACE to continue',    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "bdefs"
bdefsClock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='default text',    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
bdesq = visual.TextStim(win=win, ori=0, name='bdesq',
    text='1 - Never or rarely\n2 - Sometimes\n3 - Often\n4 - Very often\n',    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'1', u'2', u'3', u'4'], tickHeight=-1)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='People differ in the ways they act and think in different situations. This is a test\nto measure some of the ways in which you act and think. Read each statement and choose an appropriate option.\nDo not spend too much time on any\nstatement. Answer quickly and honestly.\nPress SPACE to continue.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "bis"
bisClock = core.Clock()
bis_quest = visual.TextStim(win=win, ori=0, name='bis_quest',
    text='default text',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
bis_desc = visual.TextStim(win=win, ori=0, name='bis_desc',
    text='1 = Rarely/Never\n2 = Occasionally \n3 = Often\n4 = Almost always/Always',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
bis_rating = visual.RatingScale(win=win, name='bis_rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=[u'1', u'2', u'3', u'4'], tickHeight=-1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "hand"-------
t = 0
handClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
rating_2.reset()
# keep track of which components have finished
handComponents = []
handComponents.append(text_5)
handComponents.append(rating_2)
for thisComponent in handComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "hand"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = handClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    # *rating_2* updates
    if t >= 0.0 and rating_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_2.tStart = t  # underestimates by a little under one frame
        rating_2.frameNStart = frameN  # exact frame index
        rating_2.setAutoDraw(True)
    continueRoutine &= rating_2.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in handComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "hand"-------
for thisComponent in handComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_2.response', rating_2.getRating())
thisExp.addData('rating_2.rt', rating_2.getRT())
thisExp.nextEntry()
# the Routine "hand" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "lang"-------
t = 0
langClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
langComponents = []
langComponents.append(text_3)
langComponents.append(rating)
for thisComponent in langComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lang"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = langClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t  # underestimates by a little under one frame
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in langComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lang"-------
for thisComponent in langComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
# the Routine "lang" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(text_6)
instructionsComponents.append(key_resp_5)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=75, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('expcond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    dots.setFieldCoherence(coh)
    dots.setDir(direct)
    sound_1.setVolume(vol)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text)
    trialComponents.append(dots)
    trialComponents.append(sound_1)
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        if text.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *dots* updates
        if t >= 0.5 and dots.status == NOT_STARTED:
            # keep track of start time/frame for later
            dots.tStart = t  # underestimates by a little under one frame
            dots.frameNStart = frameN  # exact frame index
            dots.setAutoDraw(True)
        if dots.status == STARTED and t >= (0.5 + (1.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            dots.setAutoDraw(False)
        # start/stop sound_1
        if t >= soa and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED and t >= (soa + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            sound_1.stop()  # stop the sound (if longer than duration)
        
        # *key_resp_2* updates
        if t >= 0.5 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED and t >= (0.5 + (1.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_2.status = STOPPED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp_2.corr:#stored on last run routine
      scores = scores + 100
      msg ="Correct! You have earned 100 points. Your total is {}".format(scores)
      #add hundred points 
    else:
      scores = scores - 50
      msg ="Oops! That was wrong. You have lost 50 points. Your score is {}".format(scores)
      #penalize by 50 points 
    
    
    
    feedbackmsg.setText(msg)
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(feedbackmsg)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedbackmsg* updates
        if t >= 0.0 and feedbackmsg.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackmsg.tStart = t  # underestimates by a little under one frame
            feedbackmsg.frameNStart = frameN  # exact frame index
            feedbackmsg.setAutoDraw(True)
        if feedbackmsg.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            feedbackmsg.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print(cumulative)
    thisExp.nextEntry()
    
# completed 75 repeats of 'trials'


#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(text_2)
instr1Components.append(key_resp_3)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
caarsq = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ADHD Qs.xlsx.xlsx'),
    seed=None, name='caarsq')
thisExp.addLoop(caarsq)  # add the loop to the experiment
thisCaarsq = caarsq.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisCaarsq.rgb)
if thisCaarsq != None:
    for paramName in thisCaarsq.keys():
        exec(paramName + '= thisCaarsq.' + paramName)

for thisCaarsq in caarsq:
    currentLoop = caarsq
    # abbreviate parameter names if possible (e.g. rgb = thisCaarsq.rgb)
    if thisCaarsq != None:
        for paramName in thisCaarsq.keys():
            exec(paramName + '= thisCaarsq.' + paramName)
    
    #------Prepare to start Routine "caars"-------
    t = 0
    caarsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    caars_quest.setText(question)
    caars_rating.reset()
    # keep track of which components have finished
    caarsComponents = []
    caarsComponents.append(caars_quest)
    caarsComponents.append(caars_desc)
    caarsComponents.append(caars_rating)
    for thisComponent in caarsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "caars"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = caarsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *caars_quest* updates
        if t >= 0.0 and caars_quest.status == NOT_STARTED:
            # keep track of start time/frame for later
            caars_quest.tStart = t  # underestimates by a little under one frame
            caars_quest.frameNStart = frameN  # exact frame index
            caars_quest.setAutoDraw(True)
        
        # *caars_desc* updates
        if t >= 0.0 and caars_desc.status == NOT_STARTED:
            # keep track of start time/frame for later
            caars_desc.tStart = t  # underestimates by a little under one frame
            caars_desc.frameNStart = frameN  # exact frame index
            caars_desc.setAutoDraw(True)
        # *caars_rating* updates
        if t >= 0.0 and caars_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            caars_rating.tStart = t  # underestimates by a little under one frame
            caars_rating.frameNStart = frameN  # exact frame index
            caars_rating.setAutoDraw(True)
        continueRoutine &= caars_rating.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in caarsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "caars"-------
    for thisComponent in caarsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for caarsq (TrialHandler)
    caarsq.addData('caars_rating.response', caars_rating.getRating())
    caarsq.addData('caars_rating.rt', caars_rating.getRT())
    # the Routine "caars" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'caarsq'


#------Prepare to start Routine "instr_bdefs"-------
t = 0
instr_bdefsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
instr_bdefsComponents = []
instr_bdefsComponents.append(text_7)
instr_bdefsComponents.append(key_resp_6)
for thisComponent in instr_bdefsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr_bdefs"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr_bdefsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_bdefsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr_bdefs"-------
for thisComponent in instr_bdefsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "instr_bdefs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bdefs.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    #------Prepare to start Routine "bdefs"-------
    t = 0
    bdefsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_8.setText(bdefq)
    rating_3.reset()
    # keep track of which components have finished
    bdefsComponents = []
    bdefsComponents.append(text_8)
    bdefsComponents.append(bdesq)
    bdefsComponents.append(rating_3)
    for thisComponent in bdefsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "bdefs"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = bdefsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        
        # *bdesq* updates
        if t >= 0.0 and bdesq.status == NOT_STARTED:
            # keep track of start time/frame for later
            bdesq.tStart = t  # underestimates by a little under one frame
            bdesq.frameNStart = frameN  # exact frame index
            bdesq.setAutoDraw(True)
        # *rating_3* updates
        if t >= 0.0 and rating_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_3.tStart = t  # underestimates by a little under one frame
            rating_3.frameNStart = frameN  # exact frame index
            rating_3.setAutoDraw(True)
        continueRoutine &= rating_3.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bdefsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "bdefs"-------
    for thisComponent in bdefsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('rating_3.response', rating_3.getRating())
    trials_4.addData('rating_3.rt', rating_3.getRT())
    # the Routine "bdefs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


#------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
instr2Components = []
instr2Components.append(text_4)
instr2Components.append(key_resp_4)
for thisComponent in instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('biss.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    #------Prepare to start Routine "bis"-------
    t = 0
    bisClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    bis_quest.setText(bisq)
    bis_rating.reset()
    # keep track of which components have finished
    bisComponents = []
    bisComponents.append(bis_quest)
    bisComponents.append(bis_desc)
    bisComponents.append(bis_rating)
    for thisComponent in bisComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "bis"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = bisClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bis_quest* updates
        if t >= 0.0 and bis_quest.status == NOT_STARTED:
            # keep track of start time/frame for later
            bis_quest.tStart = t  # underestimates by a little under one frame
            bis_quest.frameNStart = frameN  # exact frame index
            bis_quest.setAutoDraw(True)
        
        # *bis_desc* updates
        if t >= 0.0 and bis_desc.status == NOT_STARTED:
            # keep track of start time/frame for later
            bis_desc.tStart = t  # underestimates by a little under one frame
            bis_desc.frameNStart = frameN  # exact frame index
            bis_desc.setAutoDraw(True)
        # *bis_rating* updates
        if t >= 0.0 and bis_rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            bis_rating.tStart = t  # underestimates by a little under one frame
            bis_rating.frameNStart = frameN  # exact frame index
            bis_rating.setAutoDraw(True)
        continueRoutine &= bis_rating.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bisComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "bis"-------
    for thisComponent in bisComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('bis_rating.response', bis_rating.getRating())
    trials_3.addData('bis_rating.rt', bis_rating.getRT())
    # the Routine "bis" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
