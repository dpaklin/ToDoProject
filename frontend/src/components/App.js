import React from 'react';
import { Container } from '@mui/material';
import { Box } from '@mui/material';

import Header from './Header';
import Footer from './Footer';
import { UsersList } from './UsersList';

function App() {
    return (
        <Box className="App">
            <Box className="content">
                <Header />
                <Container
                    sx={{mt: 1}}
                >
                    <UsersList />
                </Container>
            </Box>
            <Footer />
        </Box>
    );
}

export default App;