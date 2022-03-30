# Game Studio Website

## Project Overview

### Major Features

**Studio News** - Find out about upcoming games, current projects, and anything else studio related. A place for the studio to publish news posts. Users can interact with and comment on posts.

**User System** - Register a new account, securely log in, and view limited access portions of the site.

**Customizable Profile** - Customize your user profile with info about yourself, and high scores and achievements earned in game.

**The Game** - Play the game, have fun! A top-down tank/maze game.

**Leaderboard** - View the users who have scored best in the game, try to earn a spot!

### Problems Solved
- The studio can share information with fans
- Users can interact with the studio and other fans
- Users can play game(s) for entertainment

### Libraries and Frameworks
- Django (4.0.3)
- Django-environ (0.8.1)
- DjangoRestFramework (3.13.1)
- Vue
- Materialize

## Features
**Studio News**
- Create news posts similar to a blog
- Comment and vote-up news posts

**User System**
- Register a new account
- Log in and out of account
- Access to pages requiring authentication

**Customizable Profile**
- Personalize profile with bio and other info
- Display high scores and achievements

**The Game**
- Control a tank and move through the level
- Defeat enemies and find power-ups
- Reach the exit to complete the level

**Leaderboard**
- View all-time high scores as well as recent high scores
- Score high enough in the game and achieve a spot on the leaderboard

### User Stories
- As an admin user, I want to add news posts and publish them at a specified time.
- As an admin user, I want to edit news posts.
- As an admin user, I want to delete news posts.
- As any user, I want to read news posts from the studio.
- As any user, I want to register a new account.
- As any user, I want to securely log into my account.
- As a registered user, I want to comment on news posts.
- As a registered user, I want to read other users comments.
- As a registered user, I want to be able to edit my past comments.
- As a registered user, I want to vote-up news posts.

- As a registered user, I want to customize my profile with information about myself.
- As a registered user, I want to display high scores and achievements on my profile.
- As a registered user, I want to read other user's profiles.

- As a user, I want to play the game.
- As a registered user, I want to earn a high score in the game.
- As a registered user, I want to unlock an achievement in the game.

- As a user, I want to view the leaderboard for the game.
- As a user, I want to sort the leaderboard by recent high scores.


## Data Model

**User**

    created_at
    is_admin
    first_name
    last_name
    email

**Post**

    created_at
    published_at
    title
    body
    author_id
    votes

**Comment**

    created_at
    body
    post_id
    author_id

**GameScore**

    created_at
    score
    game_id
    user_id

**GameAchievement**

    created_at
    name
    description
    game_id
    user_id

**UserInfo**

    bio_text
    user_id

**GameInfo**

    created_at
    name
    description

## API Endpoints

_(+ Endpoint is open)_

_(- Endpoint requires authorization)_

**Post**

    - New
    + Get
    + Get List
    - Edit
    - Vote
    - Delete

**Comment**

    - New
    - Get
    - Get List
    - Edit

**UserInfo**

    - Get
    - Edit

**GameScore**

    - New
    + Get
    + Get List

**GameAchievement**

    - New
    - Get
    - Get List

## Schedule

### Project Lifecyle
~Project proposal~

*(3/28/2022)*

~Project architecture and systems design~

*(3/29/2022)*

~Project boilerplate and library/framework setup~

*(3/30/2022)*

Sprint 1: User system and studio news

*(4/05/2022)*

Sprint 2: Customizeable user profile

*(4/08/2022)*

Sprint 3: The game

*(4/11/2022)*

Sprint 4: Leaderboard and game-site interactions

*(4/13/2022)*

Project Deployment

*(4/14/2022)*

### Milestones

**First milestone:** User system and studio news

**Second milestone:** Customizeable user profile

**Third milestone:** The game

**Fourth milestone:** Leaderboard and game-site interactions
