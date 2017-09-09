#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04),
    on September 09, 2017, at 12:20
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'stopsignaltask_key'  # from the Builder filename that created this script
expInfo = {u'Gender(m/f/o)': u'', u'Age': u'', u'UIN': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
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
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
right = visual.Rect(
    win=win, name='right',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0.8, 0.8],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
left = visual.Rect(
    win=win, name='left',
    width=[0.5,0.5][0], height=[0.5,0.5][1],
    ori=0, pos=[-0.8, 0.8],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
dots = visual.DotStim(
    win=win, name='dots',
    nDots=100, dotSize=2,
    speed=0.05, dir=1.0, coherence=1.0,
    fieldPos=(0.0, 0.0), fieldSize=0.85,fieldShape='circle',
    signalDots='same', noiseDots='direction',dotLife=3,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=1,
    depth=-3.0)
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1.0)
mouse = event.Mouse(win=win)
x, y = [None, None]


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('expcond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    dots.setFieldCoherence(coh)
    dots.setDir(direct)
    dots.refreshDots()
    sound_1.setVolume(vol)
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    
    # keep track of which components have finished
    trialComponents = [fix, right, left, dots, sound_1, mouse]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix.status == STARTED and t >= frameRemains:
            fix.setAutoDraw(False)
        
        # *right* updates
        if t >= 0.5 and right.status == NOT_STARTED:
            # keep track of start time/frame for later
            right.tStart = t
            right.frameNStart = frameN  # exact frame index
            right.setAutoDraw(True)
        frameRemains = 0.5 + 1.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if right.status == STARTED and t >= frameRemains:
            right.setAutoDraw(False)
        
        # *left* updates
        if t >= 0.5 and left.status == NOT_STARTED:
            # keep track of start time/frame for later
            left.tStart = t
            left.frameNStart = frameN  # exact frame index
            left.setAutoDraw(True)
        frameRemains = 0.5 + 1.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if left.status == STARTED and t >= frameRemains:
            left.setAutoDraw(False)
        
        # *dots* updates
        if t >= 0.5 and dots.status == NOT_STARTED:
            # keep track of start time/frame for later
            dots.tStart = t
            dots.frameNStart = frameN  # exact frame index
            dots.setAutoDraw(True)
        frameRemains = 0.5 + 1.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if dots.status == STARTED and t >= frameRemains:
            dots.setAutoDraw(False)
        # start/stop sound_1
        if t >= soa and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        frameRemains = soa + 0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sound_1.status == STARTED and t >= frameRemains:
            sound_1.stop()  # stop the sound (if longer than duration)
        # *mouse* updates
        if (fix.status==FINISHED) and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        if mouse.status == STARTED and t >= (mouse.tStart + 1.1):
            mouse.status = STOPPED
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            mouse.leftButton.append(buttons[0])
            mouse.midButton.append(buttons[1])
            mouse.rightButton.append(buttons[2])
            mouse.time.append(trialClock.getTime())
        if fix.status == FINISHED:
            for stimulus in [right,left]:
        
        # check if the mouse is pressed within the current one:
                    if mouse.isPressedIn(stimulus):
                # Yes, so store the reaction time in the data:
                        buttons, times = mouse.getPressed(getTime=True)
                        rt_exp=times[0]
                        thisExp.addData('RT_exp', rt_exp)
                        thisExp.addData('buttonpress', times)
                        respmade = stimulus.name
                        thisExp.addData('response', respmade)
        
                    # check if the stimulus' image filename matches the correct answer:
                        if stimulus.name == corrAns:
                            corresp = 1
                            thisExp.addData('correct', corresp)
                        else:
                            corresp = 0
                            thisExp.addData('correct', corresp)
        
                    # end the trial once done here:
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # store data for trials (TrialHandler)
    trials.addData('mouse.x', mouse.x)
    trials.addData('mouse.y', mouse.y)
    trials.addData('mouse.leftButton', mouse.leftButton)
    trials.addData('mouse.midButton', mouse.midButton)
    trials.addData('mouse.rightButton', mouse.rightButton)
    trials.addData('mouse.time', mouse.time)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
