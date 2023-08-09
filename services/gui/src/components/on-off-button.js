import React, { useState } from 'react';
import axios from 'axios';

const ButtonComponent = () => {
    const [isPressed, setIsPressed] = useState(true);

    const handleButtonClick = async () => {
        try {
            if (isPressed) {
                await axios.post('http://10.143.187.10:8888/off');
            } else {
                await axios.post('http://10.143.187.10:8888/on');
            }
            setIsPressed(!isPressed);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const buttonStyle = {
        backgroundColor: isPressed ? 'pink' : 'white',
        border: 'none',
        width: '120px', // Set the width to achieve a symmetrical circle
        height: '120px', // Set the height to achieve a symmetrical circle
        borderRadius: '50%', // Make the button perfectly round
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    };

    const iconStyle = {
        fontSize: '36px',
        marginRight: '5px',
        verticalAlign: 'middle',
    };

    return (
        <button style={buttonStyle} onClick={handleButtonClick}>
            <i className="fa fa-lightbulb-o" style={iconStyle} />
            {isPressed ? 'Turn Off' : 'Turn On'}
        </button>
    );
};

export default ButtonComponent;
