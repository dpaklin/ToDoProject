import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableContainer,
    TableRow,
    Paper,
    Typography,
} from '@material-ui/core';

import { fetchUsers } from '../store/authSlice';

export const UserItems = ({ users }) => {
    return users.map((user, idx) => (
        <TableRow key={idx}>
            <TableCell>{user.username}</TableCell>
            <TableCell>{user.first_name}</TableCell>
            <TableCell>{user.last_name}</TableCell>
            <TableCell>{user.email}</TableCell>
        </TableRow>
    ));
};

export const UsersList = () => {
    const dispatch = useDispatch();
    const status = useSelector((state) => state.auth.status);
    const users = useSelector((state) => state.auth.users);

    useEffect(() => {
        if (status === 'idle') {
            dispatch(fetchUsers());
        }
    }, [status, dispatch]);

    let content;

    if (status === 'loading') {
        content = <div className="loader">Загрузка...</div>;
    } else if (status === 'failed') {
        content = <div className="error">Ошибка!</div>;
    } else if (status === 'succeeded') {
        content = (
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Username</TableCell>
                            <TableCell>First Name</TableCell>
                            <TableCell>Last Name</TableCell>
                            <TableCell>Email</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        <UserItems users={users} />
                    </TableBody>
                </Table>
            </TableContainer>
        );
    }

    return (
        <section className="usersList">
            <Typography variant="h4" component="h3" sx={{ my: 3 }}>
                Пользователи
            </Typography>
            {content}
        </section>
    );
};