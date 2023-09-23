import React from 'react';

import { Autocomplete } from '@react-google-maps/api';
import { AppBar, Toolbar, Typography, InputBase, Box } from '@mui/material';
import { Search } from '@mui/icons-material';

import useStyles from './styles';
const google = window.google;
const Header = () => {
    const classes = useStyles();
    return (
        <AppBar position='static'>
            <Toolbar className={classes.toolbar}>
                <Typography variant='h5' className={classes.title}>
                    Travel Advisor
                </Typography>
                <Box display="flex">
                    <Typography variant='h6' className={classes.title}>
                        Explore New Places
                    </Typography>
                    <Autocomplete>
                        <div className={classes.search}>
                            <div className={classes.searchIcon}>
                                <Search />
                            </div>
                            <InputBase placeholder='Search....' classes={{ root: classes.inputRoot, input:classes.inputInput}}></InputBase>
                        </div>
                    </Autocomplete>
                </Box>
            </Toolbar>
        </AppBar>
    )
}

export default Header;