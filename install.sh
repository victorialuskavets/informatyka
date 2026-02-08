#!/bin/bash
# Автоматичне створення символічних посилань
ln -sf ~/dotfiles/.bashrc ~/.bashrc
ln -sf ~/dotfiles/.tmux.conf ~/.tmux.conf
echo "Dotfiles успішно підключено!"
