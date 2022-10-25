import React from 'react';
import { AppBar, Container, Toolbar, Typography } from '@material-ui/core';

const Footer = () => {
    return (
        <AppBar
            enableColorOnDark
            position="static"
            sx={{ backgroundColor: '#393939' }}
        >
            <Container maxWidth="lg">
                <Toolbar>
                    <Typography variant="body1" color="inherit">
                        ToDoProject &reg; 2022
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    );
};

export default Footer;