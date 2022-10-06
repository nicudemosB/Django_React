import React, { Component } from 'react'
import { render } from 'react-dom'
import HomePage from './HomePage'
import RoomJoinPage from './RoomJoinPage'
import CreateRoomPage from './CreateRoomPage'


// This is how you make a class in React
export default class App extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (<div>
        <HomePage />
        <RoomJoinPage />
        <CreateRoomPage />
        </div>
        )
    }
}

const appDiv = document.getElementById('app')
render(<App />, appDiv)