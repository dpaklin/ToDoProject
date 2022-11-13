import { AppBar, IconButton, Toolbar, Typography } from '@material-ui/core';
import { AccountCircle } from '@material-ui/icons';

import React from 'react';

function Header(props) {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" component="span" sx={{ flexGrow: 1 }}>
                    ToDoProject
                </Typography>
                <IconButton color="inherit">
                    <AccountCircle />
                </IconButton>
            </Toolbar>
        </AppBar>
    );
}

export default Header;